//[custom Javascript]
//Project:	Amaze - Responsive Bootstrap 4 Template
//Version:  1.0
//Last change:  15/12/2017
//Primary use:	Oreo - Responsive Bootstrap 4 Template
//should be included in all pages. It controls some layout


//===============================================================================
$(function () { $(".knob").knob({ draw: function () { if ("tron" == this.$.data("skin")) { var t, i = this.angle(this.cv), s = this.startAngle, h = this.startAngle, r = h + i, e = !0; return this.g.lineWidth = this.lineWidth, this.o.cursor && (h = r - .3) && (r += .3), this.o.displayPrevious && (t = this.startAngle + this.angle(this.value), this.o.cursor && (s = t - .3) && (t += .3), this.g.beginPath(), this.g.strokeStyle = this.previousColor, this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, s, t, !1), this.g.stroke()), this.g.beginPath(), this.g.strokeStyle = e ? this.o.fgColor : this.fgColor, this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, h, r, !1), this.g.stroke(), this.g.lineWidth = 2, this.g.beginPath(), this.g.strokeStyle = this.o.fgColor, this.g.arc(this.xy, this.xy, this.radius - this.lineWidth + 1 + 2 * this.lineWidth / 3, 0, 2 * Math.PI, !1), this.g.stroke(), !1 } } }) });
//===============================================================================
$(function () {
    $('#world-map-markers').vectorMap({
        map: 'world_mill_en',
        normalizeFunction: 'polynomial',
        hoverOpacity: 0.7,
        hoverColor: false,
        backgroundColor: 'transparent',
        regionStyle: {
            initial: {
                fill: 'rgba(210, 214, 222, 1)',
                "fill-opacity": 1,
                stroke: 'none',
                "stroke-width": 0,
                "stroke-opacity": 1
            },
            hover: {
                fill: 'rgba(255, 193, 7, 2)',
                cursor: 'pointer'
            },
            selected: {
                fill: 'yellow'
            },
            selectedHover: {}
        },
        markerStyle: {
            initial: {
                fill: '#fff',
                stroke: '#FFC107 '
            }
        },
        markers: [{
            latLng: [37.09, -95.71],
            name: 'America'
        },
        {
            latLng: [51.16, 10.45],
            name: 'Germany'
        },
        {
            latLng: [-25.27, 133.77],
            name: 'Australia'
        },
        {
            latLng: [56.13, -106.34],
            name: 'Canada'
        },
        {
            latLng: [20.59, 78.96],
            name: 'India'
        },
        {
            latLng: [55.37, -3.43],
            name: 'United Kingdom'
        },
        ]
    });
});

// Stacked Area
$(document).ready(function() {
    var options = {
        chart: {
            height: 300,
            type: 'area',
            stacked: true,
            toolbar: {
                show: false,
            },
            events: {
                selection: function(chart, e) {
                console.log(new Date(e.xaxis.min) )
                }
            },
        },

        colors: ['#59c4bc', '#ff7f81', '#e4bd51'],
        dataLabels: {
            enabled: false
        },

        series: [
            {
                name: 'Mobile',
                data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
                    min: 10,
                    max: 60
                })
            },{
                name: 'Laptop',
                data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
                    min: 10,
                    max: 20
                })
            },{
                name: 'Tablet',
                data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
                    min: 10,
                    max: 15
                })
            }
        ],

        fill: {
            type: 'gradient',
            gradient: {
                opacityFrom: 0.6,
                opacityTo: 0.8,
            }
        },

        legend: {
            position: 'top',
            horizontalAlign: 'right',
            show: true,
        },
        xaxis: {
            type: 'datetime',            
        },
        grid: {
            yaxis: {
                lines: {
                    show: false,
                }
            },
            padding: {
                top: 20,
                right: 0,
                bottom: 0,
                left: 0
            },
        },
        stroke: {
            show: true,
            curve: 'smooth',
            width: 2,
        },
    }

    var chart = new ApexCharts(
        document.querySelector("#apex-stacked-area"),
        options
    );
    chart.render();
    function generateDayWiseTimeSeries(baseval, count, yrange) {
        var i = 0;
        var series = [];
        while (i < count) {
            var x = baseval;
            var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

            series.push([x, y]);
            baseval += 86400000;
            i++;
        }
        return series;
    }
});

