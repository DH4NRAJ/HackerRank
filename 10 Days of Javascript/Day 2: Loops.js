function vowelsAndConsonants(s) {
    var vowels = ['a', 'e', 'i', 'o', 'u'];
    for(var ch of s){
        if(vowels.includes(ch)){
            console.log(ch);
        }
    }
    for(var ch of s){
        if(!vowels.includes(ch)){
            console.log(ch);
        }
    }
}
