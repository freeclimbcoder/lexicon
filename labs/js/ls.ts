let sleepIn = (weekday:boolean, vacation:boolean): boolean => {
    return !weekday||vacation
   }

let monkeyTrouble = (aSmile:boolean, bSmile:boolean): boolean => {
    return aSmile!=bSmile
}

let stringTimes = (str:string, n:number): string => {
    return str.repeat(n)
}

let luckySum = (a: number, b:number, c:number): number => {
    if (a == 13) return 0
    if (b == 13) return a
    if (c == 13) return a + b
    return a+b+c
}

let caught_speeding = (speed: number, is_birthday:boolean): number =>{
    if (is_birthday) speed-=5
    if (speed <= 60) return 0
    if (speed <= 80) return 1
    return 2

}


console.log(sleepIn(false, false))
console.log(sleepIn(true, false))
console.log(sleepIn(false, true))


console.log(caught_speeding(60, false))
console.log(caught_speeding(65, false)) 
console.log(caught_speeding(86, true))