const fs = require('fs')
const process = require('process')

const file_name = process.argv[1]

var readable = fs.createReadStream(file_name, {
    encoding: 'utf8',
    fd: null,
})
readable.on('readable', function() {
    var chunk
    while ((chunk = readable.read(1)) !== null){
        process.stdout.write(chunk) 
    }
})

readable.on('end', () => {
    console.log('\nEOF') // will be printed if there is no more data
})