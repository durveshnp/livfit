// var xmlhttp = new XMLHttpRequest();
// var url = "http://localhost/bar-chart/js/jsonData.json";
// xmlhttp.open("GET",url,true);
// xmlhttp.send();
// xmlhttp.onreadystatechange = function()
// {
//     if(this.readyState == 4 && this.status == 200)
//     {
//         var data = JSON.parse(this.responseText);
//         console.log(data);
//     }
// }





const ctx = document.getElementById('canvas').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor:"#ff335e",
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});