import foo from "./modules.ts"
import {foo1, foo2} from "./modules.ts"

console.log(foo(7));
console.log(foo1(7));
console.log(foo2(7));

// przy defaultowym exporcie możemy eksportować tylko jeden moduł
// jeżli eksportujemy bez default, to może to być kilka modułów, ale nie musimy ich wszystkich importować