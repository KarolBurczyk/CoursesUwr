function getLastProto(obj) {
    let proto = Object.getPrototypeOf(obj);
    while (Object.getPrototypeOf(proto) !== null) {
        obj = proto;
        proto = Object.getPrototypeOf(obj);
    }
    return obj;
}

const obj1 = {index: "1"};
const obj2 = {index: "2"};
const obj3 = {index: "3"};

Object.setPrototypeOf(obj3, obj2);
Object.setPrototypeOf(obj2, obj1);

const lastProto1 = getLastProto(obj1);
const lastProto2 = getLastProto(obj2);
const lastProto3 = getLastProto(obj3);


console.log(lastProto1);
console.log(lastProto2);
console.log(lastProto3);

