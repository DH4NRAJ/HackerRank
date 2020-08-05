
function Rectangle(a, b) {
    var perimeter = 2*(a+b);
    var area = a*b;
    var length = a;
    var width = b;
    var rec = {length, width, perimeter, area};
    return rec;
}
// or 
// {
//   this.length = a;
//   this.width = b;
//   this.area = a * b;
//   this.perimeter = 2 * (a + b);
// }
