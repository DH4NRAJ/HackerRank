function sides(literals, ...expressions) {
    var area = expressions[0];
    var peri = expressions[1];

    
    var s1 = (peri - Math.sqrt((peri*peri)-(16*area)))/4;
    var s2 = (peri + Math.sqrt((peri*peri)-(16*area)))/4;
    return [s1, s2];
}
