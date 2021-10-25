$(function() {
    "use strict";

    $('.sparkbar').sparkline('html', { type: 'bar' });

    // Patients Analytics Report
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#google-analytics-dashboard', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 110, 80, 202, 108, 190, 69, 109, 118, 107, 132, 91, 120],
                    ['data2', 79, 71, 55, 175, 99, 182, 82, 122, 118, 109, 86, 107],
                    ['data3', 19, 7, 25, 15, 19, 12, 28, 22, 18, 19, 16, 17],
                ],
                type: 'bar', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-a1"],
                    'data2': Amaze.colors["theme-a2"],
                    'data3': Amaze.colors["theme-a4"],
                },
                names: {
                    // name of each serie
                    'data1': 'Admits',
                    'data2': 'Discharge',
                    'data3': 'Falls',
                }
            },
            axis: {
                x: {
                    type: 'category',
                    // name of each category
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
                },
            },
            bar: {
                width: 10
            },
            legend: {
                show: true, //hide legend
            },
            padding: {
                left: 0,
                right: 0,
                bottom: 0,
                top: 0
            },
        });
    });

    //  Use by Patients Age
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Use-by-PatientsAge', // id of chart wrapper
            data: {
                type: 'pie', // default type of chart
                columns: [
                    // each columns data
                    ['data1', 15],
                    ['data2', 5],
                    ['data3', 25],
                    ['data4', 55],
                ],
                colors: {
                    'data1': Amaze.colors["theme-a1"],
                    'data2': Amaze.colors["theme-a2"],
                    'data3': Amaze.colors["theme-a3"],
                    'data4': Amaze.colors["theme-a4"]
                },
                names: {
                    // name of each serie
                    'data1': '0-10',
                    'data2': '10-30',
                    'data3': '30-50',
                    'data4': '50-up',
                }
            },
            axis: {
            },
            legend: {
                show: true, //hide legend
            },
            padding: {
                bottom: 0,
                top: 0
            },
        });
    });    

    // Use by Gander
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Use-by-gander', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 73],
                    ['data2', 27],
                ],
                type: 'donut', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-a1"],
                    'data2': Amaze.colors["theme-a4"],
                },
                names: {
                    // name of each serie
                    'data1': 'Male',
                    'data2': 'Female',
                }
            },
            axis: {
            },
            legend: {
                show: true, //hide legend
            },
            padding: {
                bottom: 0,
                top: 0
            },
        });
    });

    // Patient history
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Patient-history', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 11, 8, 15, 18, 19, 17, 11, 8, 15, 18, 19, 17],
                    ['data2', 12, 11, 8, 15, 18, 7, 7, 5, 7, 9, 19, 17],
                    ['data3', 7, 7, 5, 7, 9, 12, 7, 7, 5, 7, 9, 12,],
                ],
                type: 'bar', // default type of chart
                groups: [
                    [ 'data1', 'data2', 'data3']
                ],
                colors: {
                    'data1': Amaze.colors["theme-a1"],
                    'data2': Amaze.colors["theme-a2"],
                    'data3': Amaze.colors["theme-a3"],
                },
                names: {
                    // name of each serie
                    'data1': 'ICU',
                    'data2': 'Cancer',
                    'data3': 'Covid-19',
                }
            },
            axis: {
                x: {
                    type: 'category',
                    // name of each category
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Set', 'Oct', 'Nov', 'Dec']
                },
            },
            bar: {
                width: 20
            },
            legend: {
                show: true, //hide legend
            },
            padding: {
                bottom: 0,
                top: 0
            },
        });
    });

    // Overall Satisfaction
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Overall-Satisfaction', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 52, 31, 19, 7, 4],
                    ['data2', 59, 38, 15, 11, 2]
                ],
                type: 'bar', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-a1"],
                    'data2': Amaze.colors["theme-a2"]
                },
                names: {
                    // name of each serie
                    'data1': '2019',
                    'data2': '2020'
                }
            },
            axis: {
                x: {
                    type: 'category',
                    // name of each category
                    categories: ['5 Star', '4 Star', '3 Star', '2 Star', '1 Star']
                },
                rotated: true,
            },
            bar: {
                width: 18
            },
            legend: {
                show: true, //hide legend
            },
            padding: {
                bottom: 0,
                top: 0
            },
        });
    });
});