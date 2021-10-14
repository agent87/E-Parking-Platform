$(function() {
    "use strict";

    $('.sparkbar').sparkline('html', { type: 'bar' });

    // Company Agent Statistics
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Company-Agent-Statistics', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 23, 33, 8, 17, 41, 37],
                    ['data2', 17, 17, 15, 17, 29, 42]
                ],
                type: 'bar', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-cyan1"],
                    'data2': Amaze.colors["theme-cyan2"]
                },
                names: {
                    // name of each serie
                    'data1': 'Buy',
                    'data2': 'Sale'
                }
            },
            axis: {
                x: {
                    type: 'category',
                    // name of each category
                    categories: ['Robert', 'Orlando', 'Brian', 'Richard', 'Frank', 'Barbara']
                },
                rotated: true,
            },
            bar: {
                width: 10
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

    // Report by Sector
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Report-by-Sector', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 63],
                    ['data2', 44],
                    ['data3', 12],
                    ['data4', 14]
                ],
                type: 'pie', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-cyan1"],
                    'data2': Amaze.colors["theme-cyan2"],
                    'data3': Amaze.colors["theme-cyan3"],
                    'data4': Amaze.colors["theme-cyan4"]
                },
                names: {
                    // name of each serie
                    'data1': 'Apartment',
                    'data2': 'House',
                    'data3': 'Bungalow',
                    'data4': 'Office'
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

    // map
    var mapData = {
        "US": 298,			
        "AU": 760,
        "CA": 870,
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
				    fill : '#dfdfdf'
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
		   
            markers: [
                { latLng: [37.09,-95.71], name: 'America' },
                { latLng: [-25.27, 133.77], name: 'Australia' },
                { latLng: [55.37,-3.43], name: 'United Kingdom' },
                { latLng: [56.13,-106.34], name: 'Canada' },
            ],

			series: {
				regions: [{
					values: {
						"US": '#59c4bc',						
						"AU": '#7954ad',
                        "GB": '#2faaa1',
                        "CA": '#637aae',
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