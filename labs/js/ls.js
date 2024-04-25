let sleepIn_js = (weekday, vacation) => {
    return !weekday||vacation
   }

let monkeyTrouble_js = (aSmile, bSmile) => {
    return aSmile!=bSmile
}

let stringTimes_js = (str, n) => {
    return str.repeat(n)
}

let luckySum_js = (a, b, c) => {
    if (a == 13) return 0
    if (b == 13) return a
    if (c == 13) return a + b
    return a+b+c
}

let caught_speeding_js = (speed, is_birthday) => {
    if (is_birthday) speed-=5
    if (speed <= 60) return 0
    if (speed <= 80) return 1
    return 2

}

console.log(sleepIn_js(false, false))
console.log(sleepIn_js(true, false))
console.log(sleepIn_js(false, true))

console.log(monkeyTrouble_js(true, true))
console.log(monkeyTrouble_js(true, false))
console.log(monkeyTrouble_js(false, true))
console.log(monkeyTrouble_js(false, false))

console.log(stringTimes_js("hi",4))

console.log(luckySum_js(1,3,6))
console.log(luckySum_js(1,13,6))
console.log(luckySum_js(1,3,13))
console.log(luckySum_js(13,3,6))

console.log(caught_speeding_js(60, false))
console.log(caught_speeding_js(65, false)) 
console.log(caught_speeding_js(86, true))