from neo4j import GraphDatabase
from secret import URI, USERNAME, PASSWORD

class Neo4jManager:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def fetch_all_persons(self):
        query = "MATCH (p:Person) RETURN p.name AS Name, p.born AS BirthYear"
        with self.driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]

def print_persons_table(persons):
    print(f"{'Name':<20} | {'BirthYear':<10}")
    print("-" * 35)
    for person in persons:
        name = person.get("Name")
        birth_year = person.get("BirthYear")
        if birth_year != None:
            print(f"{name:<20} | {birth_year:<10}")
        else:
            print(f"{name:<20} | Unknown")

if __name__ == "__main__":
    neo4j_example = Neo4jManager(URI, USERNAME, PASSWORD)

    try:
        persons = neo4j_example.fetch_all_persons()

        print_persons_table(persons)
    finally:
        neo4j_example.close()
