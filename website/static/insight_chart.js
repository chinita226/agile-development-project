let colors = [
    "#BBDEFB",
    "#8D6E63",
    "#F44336",
    "#757575",
    "#F50057",
    "#FFAB00",
    "#4E342E",
    "#76FF03",
    "#0097A7",
    "#E91E63",
    "#3F51B5",
    "#F8BBD0",
    "#5D4037",
    "#BA68C8",
    "#FF7043",
    "#2979FF",
    "#69F0AE",
    "#9E9E9E",
    "#C6FF00",
    "#558B2F",
    "#FFC107",
    "#FFA000",
    "#FF3D00",
    "#C5E1A5",
    "#80DEEA",
    "#ECEFF1",
    "#64B5F6",
    "#00838F",
    "#FFAB40",
    "#CDDC39",
    "#E6EE9C",
    "#FF8F00",
    "#006064",
    "#FF5722",
    "#B3E5FC",
    "#F57C00",
    "#BF360C",

    "#F4FF81",
    "#9E9D24",
    "#FFEB3B",
    "#FFCA28",
    "#B388FF",
    "#607D8B",
    "#311B92",
    "#FF5252",
    "#689F38",
    "#2E7D32",
    "#00E676",
    "#F57F17",
    "#512DA8",
    "#AEEA00",
    "#FFD180",
    "#673AB7",
    "#8C9EFF",
    "#FF6F00",
    "#1565C0",
    "#3F51B5",
    "#42A5F5",
    "#FFCDD2",
    "#FFEA00",
    "#AFB42B",
    "#FFEB3B",
    "#9C27B0",
    "#E0F7FA",
    "#90CAF9",
    "#FFD54F",
    "#FFE0B2",
    "#03A9F4",
    "#7E57C2",
    "#004D40",
    "#DCEDC8",
    "#FFE57F",
    "#448AFF",
    "#EA80FC",
    "#00BCD4",
    "#C8E6C9",
    "#DD2C00",
    "#E1BEE7",
    "#AED581",
    "#009688",
    "#00796B",
    "#B0BEC5",
    "#66BB6A",
    "#FFEE58",
    "#FF6E40",

    "#FFAB91",
    "#40C4FF",
    "#EEEEEE",
    "#E53935",
    "#B39DDB",
    "#BCAAA4",
    "#00E5FF",
    "#F1F8E9",
    "#6200EA",
    "#5E35B1",
    "#FFD740",
    "#FFC400",
    "#FF6D00",
    "#A1887F",
    "#FFA726",
    "#536DFE",
    "#B71C1C",
    "#D1C4E9",
    "#FF9800",
    "#29B6F6",
    "#FF8A65",
    "#8E24AA",
    "#FFC107",
    "#00695C",
    "#E91E63",
    "#FDD835",
    "#1DE9B6",
    "#43A047",
    "#E57373",
    "#8BC34A",
    "#00897B",
    "#AB47BC",
    "#26C6DA",
    "#E1F5FE",
    "#880E4F",
    "#388E3C",
    "#A7FFEB",
    "#F3E5F5",
    "#BDBDBD",
    "#03A9F4",
    "#F48FB1",
    "#303F9F",
    "#D500F9",
    "#CE93D8",
    "#33691E",
    "#FB8C00",
    "#795548",
    "#3D5AFE",
    "#00C853",
    "#F06292",
    "#FFE082",
    "#C2185B",
    "#0091EA",
    "#F4511E",
    "#E64A19",
    "#FFECB3",
    "#64FFDA",
    "#CDDC39",
    "#9E9E9E",
    "#00ACC1",
    "#1976D2",
    "#424242",
    "#E0E0E0",
    "#00B0FF",
    "#FF9800",
    "#9FA8DA",
    "#616161",
    "#FAFAFA",
    "#7C4DFF",
    "#EEFF41",
    "#FFEBEE",
    "#64DD17",
    "#9575CD",
    "#E3F2FD",
    "#FF8A80",
    "#90A4AE",
    "#009688",
    "#7986CB",
    "#F9FBE7",
    "#212121",
    "#2196F3",
    "#FF9100",
    "#3949AB",
    "#827717",
    "#4527A0",
    "#8BC34A",
    "#795548",
    "#FFCC80",
    "#B2FF59",
    "#F5F5F5",
    "#D4E157",
    "#2196F3",
    "#6A1B9A",
    "#FFCCBC",
    "#F9A825",
    "#00BCD4",
    "#1B5E20",
    "#9CCC65",
    "#CCFF90",
    "#4FC3F7",
    "#C0CA33",
    "#C51162",
    "#1A237E",
    "#82B1FF",
    "#81C784",
    "#E8EAF6",
    "#9C27B0",
    "#FF5722",
    "#EFEBE9",
    "#D81B60",
    "#B2EBF2",
    "#EDE7F6",
    "#FFB74D",
    "#FF80AB",
    "#673AB7",
    "#283593",
    "#2962FF",
    "#84FFFF",
    "#AA00FF",
    "#01579B",
    "#80CBC4",
    "#EC407A",
    "#A5D6A7",
    "#FBE9E7",
    "#0277BD",
    "#7B1FA2",
    "#E65100",
    "#FF9E80",
    "#D32F2F",
    "#F0F4C3",
    "#4CAF50",
    "#D84315",
    "#18FFFF",
    "#FF4081",
    "#E0F2F1",
    "#EF5350",
    "#039BE5",
    "#4DD0E1",
    "#651FFF",
    "#0D47A1",
    "#FBC02D",
    "#C62828",
    "#E8F5E9",
    "#EF6C00",
    "#0288D1",
    "#CFD8DC",
    "#B9F6CA",
    "#304FFE",
    "#FFD600",
    "#FFB300",
    "#7CB342",
    "#D50000",
    "#AD1457",
    "#6D4C41",
    "#E040FB",
    "#00BFA5",
    "#5C6BC0",
    "#00B8D4",
    "#C5CAE9",
    "#26A69A",
    "#DCE775",
    "#80D8FF",
    "#1E88E5",
    "#F44336",
];

new Chart("myChart", {
    type: "bar",
    data: {

        labels: names,
        datasets: [{
            backgroundColor: colors,
            data: values,
        }]
    },
    options: {
        legend: { display: false },
        title: {
            display: true,
            text: "YUMMY SAVIOUR FOOD INSIGHT"
        },
        scales: {
            yAxes: [{
                display: true,
                ticks: {

                    max: 50,
                    suggestedMin: 0, // minimum will be 0, unless there is a lower value.
                    // OR //
                    beginAtZero: true // minimum value will be 0.
                }
            }]
        }
    }
});