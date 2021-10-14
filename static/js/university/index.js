//Project:	sAmaze- Responsive Bootstrap 4 Template
//Primary use:	Amaze - Responsive Bootstrap 4 Template

$(function() {
    "use strict";

    $('.sparkbar').sparkline('html', { type: 'bar' });

    // Total Revenue
    $(document).ready(function() {
        var options = {
            chart: {
                height: 310,
                type: 'line',
                toolbar: {
                    show: false,
                },
            },
            colors: ['#1c13a7', '#ffa845'],
            series: [{
                name: 'Fees',
                type: 'column',
                data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160]
            }, {
                name: 'Donation',
                type: 'line',
                data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16]
            }],
            stroke: {
                width: [0, 4]
            },        
            
            //labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dev'],
            labels: ['01 Aug 2020', '02 Aug 2020', '03 Aug 2020', '04 Aug 2020', '05 Aug 2020', '06 Aug 2020', '07 Aug 2020', '08 Aug 2020', '09 Aug 2020', '10 Aug 2020', '11 Aug 2020', '12 Aug 2020'],
            xaxis: {
                type: 'datetime'
            },
            yaxis: [{
                title: {
                    text: 'Fees',
                },

            }, {
                opposite: true,
                title: {
                    text: 'Donation'
                }
            }]
        }
        var chart = new ApexCharts(
            document.querySelector("#apex-chart-line-column"),
            options
        );

        chart.render();
    });

    // Our Location & Gender Ratio
    $(document).ready(function() {
        var options = {
            chart: {
                height: 270,
                type: 'donut',
            },
            labels: ["Boys", "Girls"],
            legend: {
                position: 'bottom',
                horizontalAlign: 'center',
                show: true,
            },
            colors: ['#1c13a7', '#ffa845'],
            series: [63, 37],

            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }]
        }

    var chart = new ApexCharts(
            document.querySelector("#apex-simple-donut"),
            options
        );
        
        chart.render();
    });

    /*VectorMap Init*/
    $(function() {
        "use strict";
        var mapData = {
            "US": 298,
            "SA": 200,
            "AU": 760,
            "IN": 2000000,
            "GB": 120,
        };
        
        if( $('#world-map-markers').length > 0 ){
            $('#world-map-markers').vectorMap(
            {
                map: 'world_mill_en',
                backgroundColor: 'transparent',
                borderColor: '#fff',
                borderOpacity: 0.25,
                borderWidth: 0,
                color: '#e6e6e6',
                regionStyle : {
                initial : {
                        fill : '#f4f4f4'
                    }
                },

                markerStyle: {
                    initial: {
                            r: 5,
                            'fill': '#fff',
                            'fill-opacity':1,
                            'stroke': '#000',
                            'stroke-width' : 1,
                            'stroke-opacity': 0.4
                        },
                    },
            
                markers : [{
                    latLng : [21.00, 78.00],
                    name : 'INDIA : 350'			  
                },
                {
                    latLng : [-33.00, 151.00],
                    name : 'Australia : 250'				
                },
                {
                    latLng : [36.77, -119.41],
                    name : 'USA : 250'			  
                },
                {
                    latLng : [55.37, -3.41],
                    name : 'UK   : 250'			  
                },
                {
                    latLng : [25.20, 55.27],
                    name : 'UAE : 250'			  
                }],

                series: {
                    regions: [{
                        values: {
                            "US": '#49c5b6',
                            "SA": '#667add',
                            "AU": '#50d38a',
                            "IN": '#60bafd',
                            "GB": '#ff758e',
                        },
                        attribute: 'fill'
                    }]
                },
                hoverOpacity: null,
                normalizeFunction: 'linear',
                zoomOnScroll: false,
                scaleColors: ['#000000', '#000000'],
                selectedColor: '#000000',
                selectedRegions: [],
                enableZoom: false,
                hoverColor: '#fff',
            });
        }
    });

});





