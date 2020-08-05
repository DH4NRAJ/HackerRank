function getDayName(dateString) {
    let dayName = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",                        "Saturday"];
    // Write your code here
    var d = new Date(dateString);
    return dayName[d.getDay()];
}
