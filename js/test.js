let p1 = new Promise((resolve, reject) => resolve());
setTimeout(console.log, 0, p1);