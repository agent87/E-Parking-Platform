//Project:	sAmaze- Responsive Bootstrap 4 Template
//Primary use:	Amaze - Responsive Bootstrap 4 Template

// basic-column
$(document).ready(function() {
    var options = {
        chart: {
            height: 300,
            type: 'bar',
        },
        colors: ['#59c4bc', '#613c95', '#868e96'],
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: '55%',
                endingShape: 'rounded'	
            },
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            show: true,
            width: 2,
            colors: ['transparent']
        },
        series: [{
            name: 'Net Profit',
            data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
        }, {
            name: 'Revenue',
            data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
        }, {
            name: 'Free Cash Flow',
            data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
        }],
        xaxis: {
            categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
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
        document.querySelector("#apex-basic-column"),
        options
    );

    chart.render();
});

// SIMPLE DONUT
$(document).ready(function() {
    var options = {
        chart: {
            height: 300,
            type: 'donut',
        },
        labels: ["Desktops", "Tablet", "Mobile"],
        legend: {
            position: 'bottom',
            horizontalAlign: 'center',
            show: true,
        },
        colors: ['#613c95', '#59C4BC', '#4343D3'],
        series: [60, 15, 25],

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

	if( $('#india').length > 0 ){
	$('#india').vectorMap({
			map : 'in_mill',
			backgroundColor : 'transparent',
			regionStyle : {
				initial : {
					fill : '#f4f4f4'
				}
			}
		});
	}	

	if( $('#usa').length > 0 ){
		$('#usa').vectorMap({
			map : 'us_aea_en',
			backgroundColor : 'transparent',
			regionStyle : {
				initial : {
					fill : '#f4f4f4'
				}
			}
		});
	}        
		   
	if( $('#australia').length > 0 ){        
		$('#australia').vectorMap({
			map : 'au_mill',
			backgroundColor : 'transparent',
			regionStyle : {
				initial : {
					fill : '#f4f4f4'
				}
			}
		});
	}	
	 
	if( $('#uk').length > 0 ){ 
		$('#uk').vectorMap({
			map : 'uk_mill_en',
			backgroundColor : 'transparent',
			regionStyle : {
				initial : {
					fill : '#f4f4f4'
				}
			}
		});
	}	
});

