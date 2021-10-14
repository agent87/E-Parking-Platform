$(function() {
    "use strict";

    //Salary analytics
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Salary-analytics', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 110, 80, 150, 180, 190, 170, 100, 120, 70, 90, 120, 110],
                    ['data2', 70, 100, 50, 70, 90, 120, 110, 80, 150, 180, 190, 170],
                    ['data3', 80, 60, 90, 110, 100, 120, 70, 90, 120, 110, 80, 150]
                ],
                type: 'bar', // default type of chart
                groups: [
                    [ 'data1', 'data2', 'data3']
                ],
                colors: {
                    'data1': Amaze.colors["theme-cyan1"],
                    'data2': Amaze.colors["theme-cyan2"],
                    'data3': Amaze.colors["theme-cyan3"],
                },
                names: {
                    // name of each serie
                    'data1': 'Doctors',
                    'data2': 'Nurse',                    
                    'data3': 'Contract Base',                    
                }
            },
            axis: {
                x: {
                    type: 'category',
                    // name of each category
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
                },
                y : {
                    tick: {
                        format: d3.format("$,")
        //                format: function (d) { return "$" + d; }
                    }
                }
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
});