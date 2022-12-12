
class Person{
    constructor(nome){
        this.name = nome
    }
    printarNomeDeclaration(){
        function nameIn(params) {
            console.log(this)
        }
        nameIn = nameIn.bind(this)
        nameIn()
    }
    printarNomeArrow(){
        const name = _ => {
            console.log(this)
        }
        name()
    }
}

console.log(Person)

// let pessoa = new Person("Jhnoys")
// pessoa.printarNomeArrow()
// pessoa.printarNomeDeclaration()

// const pessoa2 = () => {
//     this.fala = "EAI! COMO VAI?"
//     console.log(arguments)
// }

// pessoa2("999")

// function pessoa3(){
//     this.fala = "EAI! COMO VAI?"
//     console.log(arguments)
// }

// pessoa3("999")