const readLine = require('readline-sync')

const angka1 = Number(readLine.question("Masukkan angka pertama anda : "))
const angka2 = Number(readLine.question("Masukkan angka kedua anda : "))
const op = readLine.question("Masukan operasi anda  +  -  *  /  :  ")
const pertambahan = angka1 + angka2
const perkurangan =  angka1 - angka2
const perkalian = angka1 * angka2
const pembagian = angka1/angka2


if(op === "+") {
    console.log(pertambahan)
}else if(op === "-") {
    console.log(perkurangan)
}else if(op === '*') {
    console.log(perkalian)
}else if(op === '/') {
    console.log(pembagian)
}else {
    console.log('Tidak ada Operasi')
}
