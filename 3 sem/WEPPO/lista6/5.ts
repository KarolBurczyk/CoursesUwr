type User = {
    name: string;
    age: number;
    occupation: string;
}
type Admin = {
    name: string;
    age: number;
    role: string;
}

type Person = User | Admin;

const persons: Person[] = [
    {
        name: 'Jan Kowalski',
        age: 17,
        occupation: 'Student'
    },
    {
        name: 'Tomasz Malinowski',
        age: 20,
        role: 'Administrator'
    }
];

function logPerson(person: Person) {
    let additionalInformation: string;
    if ('role' in person) { // zamiast if person.role
        additionalInformation = person.role;
    } 
    else {
        additionalInformation = person.occupation;
    }
    console.log(` - ${ person.name }, ${ person.age }, ${ additionalInformation }`);
}

for(let i : number = 0; i < persons.length; i += 1) {
    logPerson(persons[i]);
}