const http = require('http')

const hostname = '127.0.0.1'
const port = 3000
const url = `http://${hostname}:${port}`

const server = http.createServer((request, response) => {
    console.log()
    response.statusCode = 200;
    response.setHeader('Content-Type','text/html')
    response.end('<h1>Olá Mundo!')
})

server.listen(port, hostname, () => {
    console.log(`servidor rodando em: ${url}`)
})