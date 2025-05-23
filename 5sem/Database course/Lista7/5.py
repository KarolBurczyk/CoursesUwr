from neo4j import GraphDatabase
from secret import URI, USERNAME, PASSWORD

class Person:
    def __init__(self, name, born=None):
        self.name = name
        self.born = born

    def __repr__(self):
        return f"Person(name='{self.name}', born={self.born})"


class Movie:
    def __init__(self, title, released=None):
        self.title = title
        self.released = released

    def __repr__(self):
        return f"Movie(title='{self.title}', released={self.released})"


class ActedIn:
    def __init__(self, person, movie, roles=None):
        self.person = person
        self.movie = movie
        self.roles = roles or []

    def __repr__(self):
        return f"ActedIn(person={self.person}, movie={self.movie}, roles={self.roles})"

class Neo4jManager:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def create_person(self, name, born=None):
        query = "CREATE (p:Person {name: $name, born: $born}) RETURN p"
        with self.driver.session() as session:
            result = session.run(query, name=name, born=born)
            record = result.single()
            node = record["p"]
            return Person(node["name"], node.get("born"))

    def create_movie(self, title, released=None):
        query = "CREATE (m:Movie {title: $title, released: $released}) RETURN m"
        with self.driver.session() as session:
            result = session.run(query, title=title, released=released)
            record = result.single()
            node = record["m"]
            return Movie(node["title"], node.get("released"))

    def create_relationship(self, person_name, movie_title, roles):
        query = """
        MATCH (p:Person {name: $person_name}), (m:Movie {title: $movie_title})
        CREATE (p)-[r:ACTED_IN {roles: $roles}]->(m)
        RETURN p, m, r
        """
        with self.driver.session() as session:
            result = session.run(query, person_name=person_name, movie_title=movie_title, roles=roles)
            record = result.single()
            person = Person(record["p"]["name"], record["p"].get("born"))
            movie = Movie(record["m"]["title"], record["m"].get("released"))
            return ActedIn(person, movie, roles)

    def fetch_all_persons(self):
        query = "MATCH (p:Person) RETURN p"
        with self.driver.session() as session:
            result = session.run(query)
            return [Person(record["p"]["name"], record["p"].get("born")) for record in result]

    def update_person(self, old_name, new_name):
        query = "MATCH (p:Person {name: $old_name}) SET p.name = $new_name RETURN p"
        with self.driver.session() as session:
            result = session.run(query, old_name=old_name, new_name=new_name)
            record = result.single()
            node = record["p"]
            return Person(node["name"], node.get("born"))

    def delete_person(self, name):
        query = "MATCH (p:Person {name: $name}) DETACH DELETE p"
        with self.driver.session() as session:
            session.run(query, name=name)

    def delete_movie(self, title):
        query = "MATCH (m:Movie {title: $title}) DETACH DELETE m"
        with self.driver.session() as session:
            session.run(query, title=title)

if __name__ == "__main__":

    manager = Neo4jManager(URI, USERNAME, PASSWORD)

    try:
        keanu = manager.create_person("Keanu Reeves", 1964)
        matrix = manager.create_movie("The Matrix", 1999)
        print("Created:", keanu, matrix, "\n")

        acted_in = manager.create_relationship("Keanu Reeves", "The Matrix", ["Neo"])
        print("Created Relationship:", acted_in, "\n")

        persons = manager.fetch_all_persons()
        print("All Persons:", persons, "\n")

        updated_person = manager.update_person("Keanu Reeves", "Keanu Charles Reeves")
        print("Updated Person:", updated_person, "\n")

        # manager.delete_person("Keanu Charles Reeves")
        # print("Deleted 'Keanu Charles Reeves'", "\n")

        # manager.delete_movie("The Matrix")
        # print("Deleted 'The Matrix'", "\n")
    finally:
        manager.close()
