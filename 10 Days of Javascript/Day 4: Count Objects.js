function getCount(objects) {
    var count = 0;
    for(var object in objects){
        if(objects[object].x == objects[object].y){
            count += 1;
        }
    }
    return count;
}
// {
//     return objects.filter(item => (item.x == item.y)).length;
// }
