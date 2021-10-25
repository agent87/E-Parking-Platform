$(function() {
    "use strict";

    //  Use by Device
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Properties-Analytics', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 48],
                    ['data2', 12],
                    ['data3', 25],
                    ['data4', 15],
                ],
                type: 'pie', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-cyan1"],
                    'data2': Amaze.colors["theme-cyan2"],
                    'data3': Amaze.colors["theme-cyan3"],
                    'data4': Amaze.colors["theme-cyan3"],
                },
                names: {
                    // name of each serie
                    'data1': 'Commercial',
                    'data2': 'Residential',
                    'data3': 'Purchased',
                    'data4': 'Rented',
                }
            },
            axis: {
            },
            legend: {
                show: false, //hide legend
            },
            padding: {
                bottom: 0,
                top: 0
            },
        });
    });

    // Properties Stats
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#chart-bar-rotated', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 1150, 2058, 3055, 1108, 2819, 1758],
                    ['data2', 1704, 2157, 5205, 2587, 3159, 1082]
                ],
                type: 'bar', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-cyan1"],
                    'data2': Amaze.colors["theme-cyan2"]
                },
                names: {
                    // name of each serie
                    'data1': 'Buying',
                    'data2': 'Selling'
                }
            },
            axis: {
                x: {
                    type: 'category',
                    // name of each category
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                },
                y: {
                    tick: {
                      format: d3.format('$,')
                    }
                },
                rotated: true,
            },
            bar: {
                width: 12
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
   
    // Gender-Ratio
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Gender-Ratio', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 73],
                    ['data2', 27],
                ],
                type: 'donut', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-purple1"],
                    'data2': Amaze.colors["theme-purple2"],
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
    
});
