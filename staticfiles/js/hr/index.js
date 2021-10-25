$(function() {
    "use strict";

    $('.sparkbar').sparkline('html', { type: 'bar' });

    // Income Analysis
    $(document).ready(function() {
        var options = {
            chart: {
                height: 300,
                type: 'radar',
                dropShadow: {
                    enabled: true,
                    blur: 1,
                    left: 1,
                    top: 1
                }
            },
            colors: ['#59c4bc', '#637aae', '#e4537b'],
            series: [{
                name: 'Design',
                data: [80, 50, 30, 40, 100, 20],
            }, {
                name: 'Dev',
                data: [20, 30, 40, 80, 20, 80],
            }, {
                name: 'SEO',
                data: [44, 76, 78, 13, 43, 10],
            }],
            stroke: {
                width: 0
            },
            fill: {
                opacity: 0.4
            },
            markers: {
                size: 0
            },
            labels: ['2015', '2016', '2017', '2018', '2019', '2020']
        }

        var chart = new ApexCharts(
            document.querySelector("#apex-income-analysis"),
            options
        );

        chart.render();
        function update() {
    
            function randomSeries() {
                var arr = []
                for(var i = 0; i < 6; i++) {
                    arr.push(Math.floor(Math.random() * 100)) 
                }    
                return arr
            }           
    
            chart.updateSeries([{
                name: 'Design',
                data: randomSeries(),
            }, {
                name: 'Dev',
                data: randomSeries(),
            }, {
                name: 'SEO',
                data: randomSeries(),
            }])
        }
    });

    // Salary Statistics
    $(document).ready(function() {
        var options = {
            chart: {
                height: 320,
                type: 'area',
            },
            colors: ['#59c4bc', '#637aae', '#e4537b', '#4de373'],
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '70%',
                    //endingShape: 'rounded'	
                },
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: false,
                width: 1,
                colors: ['transparent']
            },
            series: [{
                name: 'Sales',
                data: [44, 55, 57, 56, 61, 58, 63, 60, 66, 61, 63, 72]
            }, {
                name: 'Marketing',
                data: [76, 85, 101, 98, 87, 105, 91, 114, 94, 87, 88, 91]
            }, {
                name: 'Develpment',
                data: [76, 114, 94, 87, 88, 91, 98, 87, 105, 91, 85, 101]
            }, {
                name: 'Design',
                data: [35, 41, 36, 26, 45, 48, 52, 53, 41, 45, 47, 55]
            }],
            xaxis: {
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            },
            yaxis: {
                title: {
                    text: '$ (thousands)'
                }
            },
            fill: {
                opacity: 1
            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return "$ " + val + " thousands"
                    }
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#apex-salary-statistics"),
            options
        );

        chart.render();
    });

    // Satisfaction
    $(document).ready(function() {
        var options = {
            chart: {
                height: 250,
                type: 'radialBar',
                toolbar: {
                    show: true
                }
            },
            colors: ['#637aae'],
            plotOptions: {
                radialBar: {
                    startAngle: -135,
                    endAngle: 225,
                        hollow: {
                        margin: 0,
                        size: '70%',
                        background: '#fff',
                        image: undefined,
                        imageOffsetX: 0,
                        imageOffsetY: 0,
                        position: 'front',

                        dropShadow: {
                            enabled: true,
                            top: 3,
                            left: 0,
                            blur: 4,
                            opacity: 0.24
                        }
                    },
                    track: {
                        background: '#fff',
                        strokeWidth: '67%',
                        margin: 0, // margin is in pixels
                        dropShadow: {
                            enabled: true,
                            top: -3,
                            left: 0,
                            blur: 4,
                            opacity: 0.35
                        }
                    },

                    dataLabels: {
                        showOn: 'always',
                        name: {
                            offsetY: -10,
                            show: true,
                            color: '#888',
                            fontSize: '17px'
                        },
                        value: {
                            formatter: function(val) {
                                return parseInt(val);
                            },
                            color: '#111',
                            fontSize: '36px',
                            show: true,
                        }
                    }
                }
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'dark',
                    type: 'horizontal',
                    shadeIntensity: 0.5,
                    gradientToColors: ['#e4537b'],
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0, 100]
                }
            },
            series: [71],
            stroke: {
                lineCap: 'round'
            },
            labels: ['Percent'],
        }

        var chart = new ApexCharts(
            document.querySelector("#apex-employee-satisfaction"),
            options
        );

        chart.render();    
    });

    // Project Timeline
    $(document).ready(function() {
        var options = {
            chart: {
                height: 350,
                type: 'rangeBar',
                toolbar: {
                    show: false,
                }
            },        
            plotOptions: {
                bar: {
                    horizontal: true,                
                }
            },
            colors: ['#59c4bc', '#e4537b'],

            series: [{
                name: 'Web App',            
                data: [{
                    x: 'Wireframe',
                    y: [new Date('2020-09-02').getTime(), new Date('2020-09-04').getTime()]
                    }, {
                        x: 'Design',
                        y: [new Date('2020-09-03').getTime(), new Date('2020-09-07').getTime()]
                    }, {
                        x: 'Deployment',
                        y: [new Date('2020-09-02').getTime(), new Date('2020-09-11').getTime()]
                    }, {
                        x: 'Test',
                        y: [new Date('2020-09-11').getTime(), new Date('2020-09-12').getTime()]
                    }]
                },{
                name: 'iOs App',
                data: [{
                    x: 'Wireframe',
                    y: [new Date('2020-09-01').getTime(), new Date('2020-09-02').getTime()] 
                    }, {
                        x: 'Design',
                        y: [new Date('2020-09-09').getTime(), new Date('2020-09-07').getTime()] 
                    }, {
                        x: 'Deployment',
                        y: [new Date('2020-09-06').getTime(), new Date('2020-09-09').getTime()]
                    }, {
                        x: 'Test',
                        y: [new Date('2020-09-10').getTime(), new Date('2020-09-11').getTime()]
                    }]
            }],
            yaxis: {
                min: new Date('2020-09-01').getTime(),
                max: new Date('2020-09-14').getTime()
            },
            xaxis: {
                type: 'datetime'
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'light',
                    type: "vertical",
                    shadeIntensity: 0.25,
                    gradientToColors: undefined,
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [50, 0, 100, 100]
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#apex-project-timeline"),
            options
        );
        
        chart.render();
    });
   
});
