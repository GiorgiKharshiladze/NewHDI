/*=========================================================================================
    File Name: basic-scatter.js
    Description: echarts basic scatter chart
    ----------------------------------------------------------------------------------------
    Item Name: Modern Admin - Clean Bootstrap 4 Dashboard HTML Template
    Version: 1.0
    Author: PIXINVENT
    Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/

var my_hdis = [], undps = [], countries = [];

$('#data_table .country').each(function(){
    countries.push($(this).html());
});
$('#data_table .my_hdi').each(function(){
    my_hdis.push(parseInt($(this).html()));
});
$('#data_table .undp_hdi').each(function(){
    undps.push(parseInt($(this).html()));
});

var data_my_hdis = countries.map(function(e, i) {
  return [e, my_hdis[i]];
});
var data_undps = countries.map(function(e, i) {
  return [e, undps[i]];
});

// Basic scatter chart
// ------------------------------

$(window).on("load", function(){

    // Set paths
    // ------------------------------

    require.config({
        paths: {
            echarts: '../../static/app-assets/vendors/js/charts/echarts'
        }
    });


    // Configuration
    // ------------------------------

    require(
        [
            'echarts',
            'echarts/chart/scatter'
        ],


        // Charts setup
        function (ec) {
            // Initialize chart
            // ------------------------------
            var myChart = ec.init(document.getElementById('basic-scatter'));

            // Chart Options
            // ------------------------------
            chartOptions = {

                // Add tooltip
                tooltip : {
                    trigger: 'axis',
                    showDelay : 0,
                    formatter : function (params) {
                            return params[0].value[0] + '<br>' + params[0].seriesName + ' : ' + params[0].value[1] + '<br>' + params[1].seriesName + ' : ' + params[1].value[1];
                    }
                },

                // Add legend
                legend: {
                    data: ['My HDI', 'UNDP']
                },

                // Add custom colors
                color: ['#1EC481', '#FF394F'],

                // Horizontal axis
                xAxis : [
                    {
                        type : 'category',
                        axisLabel: {
                            formatter : function(v) {
                                return v
                            }
                        },
                        data : countries
                    }
                ],
                yAxis : [
                    {
                        type : 'value'
                    }
                ],

                // Add series
                 series : [
                {
                    name:'My HDI',
                    type:'scatter',
                    data: data_my_hdis,
                },
                {
                    name:'UNDP',
                    type:'scatter',
                    data: data_undps,
                }
            ]
            };

            // Apply options
            // ------------------------------

            myChart.setOption(chartOptions);


            // Resize chart
            // ------------------------------

            $(function () {

                // Resize chart on menu width change and window resize
                $(window).on('resize', resize);
                $(".menu-toggle").on('click', resize);

                // Resize function
                function resize() {
                    setTimeout(function() {

                        // Resize chart
                        myChart.resize();
                    }, 200);
                }
            });
        }
    );
});