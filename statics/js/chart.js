//扇形图

// 基于准备好的dom，初始化echarts实例
var myChart1 = echarts.init(document.getElementById('chart1'));
var data = {{ pcfd }}

    // 指定图表的配置项和数据
option = {
    backgroundColor: '#2c343c',

    title: {
        text: 'Field Distribution Of Collected Paper',
        left: 'center',
        top: 20,
        textStyle: {
            color: '#ccc'
        }
    },

    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },

	//最小值和最大值，一定记得对应的改，不然会全黑色
    visualMap: {
        show: false,
        min: 0,
        max: {{ max1 }},
        inRange: {
            colorLightness: [0, 1]
        }
    },
    series: [
        {
            name: 'Field',
            type: 'pie',
            radius: '55%',
            center: ['50%', '50%'],
            data: data.sort(function (a, b) { return a.value - b.value; }),
            roseType: 'radius',
            label: {
                color: 'rgba(255, 255, 255, 0.3)'
            },
            labelLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.3)'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
            },
            itemStyle: {
                color: '#c23531',
                shadowBlur: 200,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            },

            animationType: 'scale',
            animationEasing: 'elasticOut',
            animationDelay: function (idx) {
                return Math.random() * 200;
            }
        }
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart1.setOption(option);



//扇形图
// 基于准备好的dom，初始化echarts实例
var myChart2 = echarts.init(document.getElementById('chart2'));
var data = {{ acfd }}
 // 指定图表的配置项和数据 
option = {
    backgroundColor: '#2c343c',

    title: {
        text: 'Field Distribution Of Collected Author',
        left: 'center',
        top: 20,
        textStyle: {
            color: '#ccc'
        }
    },

    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    //最小值和最大值，一定记得对应的改，不然会全黑色
    visualMap: {
        show: false,
        min: 0,
        max: max2,
        inRange: {
            colorLightness: [0, 1]   
        }
    },
    series: [
        {
            name: 'Field',
            type: 'pie',
            radius: '55%',
            center: ['50%', '50%'],
            data: data.sort(function (a, b) { return a.value - b.value; }),
            roseType: 'radius',
            label: {
                color: 'rgba(255, 255, 255, 0.3)'
            },
            labelLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.3)'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
            },
            itemStyle: {
                color: '#c23531',
                shadowBlur: 200,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            },

            animationType: 'scale',
            animationEasing: 'elasticOut',
            animationDelay: function (idx) {
                return Math.random() * 200;
            }
        }
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart2.setOption(option);