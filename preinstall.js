var child_process = require('child_process');
var red = '\u001b[31m',
    green = '\u001b[32m',
    reset = '\u001b[0m';

var nodeGyp = function() {
  var os = require('os');

  switch (os.platform()) {
    case 'win32':
      return 'node-gyp.cmd';
    case 'linux':
    case 'darwin':
    default:
      return 'node-gyp';
  }
}

var rebuild = function() {
  try {
    var bindings = require('bindings')('sapnwrfc');
    console.log(green + 'ok ' + reset + 'found precompiled module at ' + bindings.path);
  } catch (e) {
    console.log(e);
    console.log(red + 'error ' + reset + 'a precompiled module could not be found or loaded');
    
    // Spawn gyp
    console.log(green + 'info ' + reset + 'trying to compile it...');
    var opts = {};
    opts.customFds = [ 0, 1, 2 ];
    opts.env = process.env;
    child_process.spawn(nodeGyp(), ['rebuild'], opts);
  }
}

var opts = {};
opts.customFds = [ 0, 1, 2 ];
var cp = child_process.spawn(nodeGyp(), ['clean'], opts);
cp.on('exit', rebuild);