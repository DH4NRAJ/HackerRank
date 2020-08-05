function getSecondLargest(nums) {
    // Complete the function
    var newarr = Array.from(new Set(nums));
    newarr = newarr.sort((x,y) => (x<y));
    return newarr[1];
}
