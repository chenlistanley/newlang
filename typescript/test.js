var Sex;
(function (Sex) {
    Sex[Sex["F"] = 0] = "F";
    Sex[Sex["M"] = 1] = "M";
})(Sex || (Sex = {}));
function test() {
    var a = Sex.M;
    console.log(a);
}
test();
