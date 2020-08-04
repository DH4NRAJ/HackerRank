function throwzero(){
    throw new Error("Zero Error");
}
function throwneg(){
    throw new Error("Negative Error");
}
function isPositive(a) {
    if (a == 0){
        return throwzero();
    } else if (a < 0){
        return throwneg();
    } else {
        return "YES";
    }  
}
