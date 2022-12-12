//this.ola = "fala ae"
//exports.bemVindo = "Seja bem vindo"
//module.exports.fabrica = "fabricando"

//console.log(arguments)

//let teste = (x, y) => {
//    return x < y
//}

//console.log(teste())

function test(){
    console.log("this dentro de function expression")
    this.name = "Jhonys"
    console.log(this == exports)
    console.log(this == module)
    console.log(this == module.exports)
    console.log(this == global)
}

let test2 = () => {
    console.log("this dentro de arrow function")
    this.name = "jhonys"
    console.log(this == exports)
    console.log(this == module)
    console.log(this == module.exports)
    console.log(this == global)
    console.log(arguments[0])
}

console.log("this no global")
console.log(this == exports)
console.log(this == module)
console.log(this == module.exports)
console.log(this == global)

test()
console.log("usando operador new")
let t = new test()
console.log(t.name)

test2()
