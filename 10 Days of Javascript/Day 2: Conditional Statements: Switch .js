
function getLetter(s) {
    let letter;
    let k = s[0];
    // Write your code here
    switch(true){
        case 'aeiou'.includes(k):
            letter = 'A';
            break;
        case 'bcdfg'.includes(k):
            letter ='B';
            break;
        case 'hjklm'.includes(k):
            letter = 'C';
            break;
        case 'npqrstvwxyz'.includes(k):
            letter = 'D';
            break;
    }
    return letter;
}
