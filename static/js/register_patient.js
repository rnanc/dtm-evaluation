function Checked1(checkbox) {
    var checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}

function Checked2(checkbox) {
    var checkboxes = document.getElementsByName('check2')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}

// function Checked_Y(checkbox) {
//     var checkboxes = document.getElementsByName('check3')
//     checkboxes.forEach((item) => {
//         if (item !== checkbox) item.checked = false
//     })
// }

// function Checked_N(checkbox) {
//     var checkboxes = document.getElementsByName('check4')
//     checkboxes.forEach((item) => {
//         if (item !== checkbox) item.checked = false
//     })
// }