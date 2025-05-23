type User = {
    name: string;
    age: number;
    occupation: string;
    type: string;
}
type Admin = {
    name: string;
    age: number;
    role: string;
    type: string;
}

type Person = User | Admin;

const persons: Person[] = [
    {
        name: 'Jan Kowalski',
        age: 17,
        occupation: 'Student',
        type: 'user'
    },
    {
        name: 'Tomasz Malinowski',
        age: 20,
        role: 'Administrator',
        type: 'admin'
    }
];

function isAdmin(person: Person) : person is Admin{
    return person.type == 'admin';
}

function isUser(person: Person) : person is User{
    return person.type == 'user';   
}
    

export function logPerson(person: Person) {
    let additionalInformation: string = '';
    if (isAdmin(person)) {
        additionalInformation = person.role;
    }
    if (isUser(person)) {
        additionalInformation = person.occupation;
    }
    console.log(` - ${ person.name }, ${ person.age }, ${ additionalInformation }`);
}

for(let i : number = 0; i < persons.length; i += 1) {
    logPerson(persons[i]);
}