const pyshell = require('python-shell').PythonShell

pyshell.run('Downloader.py',null,(err) => {
    if (err) {
        console.log(err)
    }
    else{
        console.log('finished')
    }
})