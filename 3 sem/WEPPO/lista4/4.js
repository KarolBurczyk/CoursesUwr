var Person = {
    constructor() {
        this.name = 'michal';
    }
};
var Worker = {
    job: "teacher"
};

Worker.prototype = Object.create( Person.prototype );
console.log(Worker.name);
Worker.prototype = Person.prototype;
console.log(Worker.name);
Worker.prototype = new Person();
console.log(Worker.name);

