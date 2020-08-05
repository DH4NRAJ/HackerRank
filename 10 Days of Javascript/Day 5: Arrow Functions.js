function modifyArray(nums) {
    // var modifyednums = nums.map(function(x){
    //     if(x%2 ==0){
    //         return x*2;
    //     }
    //     else{
    //         return x*3;
    //     }
    // })
    // return modifyednums;
    return nums.map(x => x = (x%2==0)? x*2:x*3);
}
