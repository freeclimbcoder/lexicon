class Rectangle {
    constructor(width, height, color) {
      this.width = width
      this.height = height
      this.color = color
    }
    calcArea() {
      return this.height*this.width
    }
  }
  
let rect = new Rectangle(4, 5, 'red');
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());


class Person{
  constructor(firstName, lastName, age, email){
    this.firstName = firstName
    this.lastName = lastName
    this.age = age
    this.email = email
  }
  toString(){
    return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`
  }
}

let person = new Person('Maria', 'Petterson', 22, 'mp@gmail.com')
console.log(person.toString())

let personArr = []
personArr[0] = person
personArr[1] = new Person('Lexicon')
personArr[2] = new Person('Stefan', 'Larsson', 25)
personArr[3] = new Person('Peter', 'Janson', 24, 'ptr@live.com') 

for (pers of personArr){
  console.log(pers.toString())
}


class Circle{
  constructor(radius){
    this.radius = radius
  }

  get diameter(){
    return 2*parseFloat(this.radius)
  }

  get area(){
    return 3.14*parseFloat(this.radius)**2
  }

  set diameter(value){
    this.radius = parseFloat(value)/2
  }
}

let c = new Circle(2);
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area}`);

class Point{
  constructor(x,y){
    this.x = x
    this.y = y
  }

  static distance(p1, p2){
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
  }
}

let p1 = new Point(5, 5);
let p2 = new Point(9, 8);
console.log(Point.distance(p1, p2)); 