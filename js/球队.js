function main(n, k, d1, d2) {

    var res = calcXYZ(k, d1, d2, 1, 1)
    if (test()) {
        console.log(res)
        return true
    }
    var res = calcXYZ(k, d1, d2, 1, -1)
    if (test()) {
        console.log(res)
        return true
    }
    var res = calcXYZ(k, d1, d2, -1, 1)
    if (test()) {
        console.log(res)
        return true
    }

    var res = calcXYZ(k, d1, d2, -1, -1)
    if (test()) {
        console.log(res)
        return true
    }
    return false

    function test() {
        if (res === false) return false
        var arr = [res.x, res.y, res.z]
        arr.sort(function (a, b) {
            return a - b
        })
        var min = arr[0]
        var mid = arr[1]
        var max = arr[2]

        var distance = max - min + max - mid
        var remain = n - k
        if ((remain - distance >= 0) && (remain - distance) % 3 === 0) {
            return true
        } else {
            return false
        }
    }
}



function calcXYZ(k, d1, d2, isXMoreThanY, isYMoreThanZ) {
    var x = y + isXMoreThanY * d1
    var y = (k + isYMoreThanZ * d2 - isXMoreThanY * d1) / 3
    var z = y - isYMoreThanZ * d2

    if (!isNotNegativeInteger(x) || !isNotNegativeInteger(x) || !isNotNegativeInteger(x)) {
        return false
    } else {
        return {
            x: x,
            y: y,
            z: z
        }
    }
}
//是否为非负整数 
function isNotNegativeInteger(num) {
    if (typeof (num) !== "number") return false
    if (num < 0) return false
    if (num % 1 !== 0) return false
    return true
}
function main_main(n, k, d1, d2) {
    var num = n
    console.log(num-k)
    // alert('!!')
    for (var x = 0; x < num-k; x++) {
        var arr = [n, k, d1, d2]
        for (var i = 0; i < arr.length; i++) {
            arr[i] = parseInt(arr[i])
        }
        // alert('!!')
        var out = main(n, k, d1, d2)
        if (out) {
            console.log("yes")
        } else {
            console.log("no")
        }
    }
}
