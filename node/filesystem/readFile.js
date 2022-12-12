const {readFile, readFileSync}  = require('fs')

readFile("filesystem/texto.txt", (err, data) => {
    if(err) throw err;

    // console.log(data.toString())
})

let texto = readFileSync("filesystem/texto.txt")
console.log(texto.toString())