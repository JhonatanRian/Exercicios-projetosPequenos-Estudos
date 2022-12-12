const {readdir}  = require('fs')

readdir("../", (err, data) => {
    if(err) throw err;

    data.forEach(files => {
        console.log(__dirname + '/' + files)
    });
})