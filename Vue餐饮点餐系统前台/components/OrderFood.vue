<template>
  <div >
      <el-header >
        绝妙订餐系统
      </el-header>
       <el-row>
           <el-col :span="4">
              <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                background-color="darkgreen"
                text-color="#fff"
               >
                  <el-menu-item index="1">
                        <template slot="title">
                            <i class="el-icon-s-platform"></i>
                            <span>厨师推荐</span>
                        </template>
                  </el-menu-item>
                  <el-menu-item index="2">
                        <template slot="title">
                            <i class="el-icon-s-tools"></i>
                            <span>精品凉菜</span>
                        </template>
                  </el-menu-item>
                  <el-menu-item index="3">
                        <template slot="title">
                              <i class="el-icon-user-solid"></i>
                              <span>特色小炒</span>
                        </template>
                  </el-menu-item>
                  <el-menu-item index="4">
                        <template slot="title">
                              <i class="el-icon-message-solid"></i>
                              <span>家常热菜</span>
                        </template>
                  </el-menu-item>
                  <el-menu-item index="5">
                        <template slot="title">
                              <i class="el-icon-message-solid"></i>
                              <span>营养主食</span>
                        </template>
                  </el-menu-item>
                  <el-menu-item index="6">
                        <template slot="title">
                              <i class="el-icon-message-solid"></i>
                              <span>调味饮料</span>
                        </template>
                    </el-menu-item>
              </el-menu>
          </el-col>
         <el-col :span="20">
              <el-table :data="tableData" ref="myTable">
                  <el-table-column label="菜名"  prop="name"></el-table-column>
                  <el-table-column label="菜品图片"  prop="img">
                        <template slot-scope="scope">
                          <img :src="scope.row.img" width="170" height="124"/>
                        </template>
                  </el-table-column>
                  <el-table-column label="菜品价格"  prop="price"></el-table-column>
              </el-table>
         </el-col>

      </el-row>
      <el-row>

            <el-col :span="2">
              <div class="bg-green-dark">
                  <i class="el-icon-cart"></i>
              </div>
            </el-col>
            <el-col :span="18">
              <div class="bg-green-dark">
                商品4件，20.00元
              </div>
            </el-col>
            <el-col :span="4">
              <div class="bg-red-dark">
                去结算
              </div>
            </el-col>
      </el-row>

  </div>
</template>

<script>
  import "../assets/logo.png"
export default {
   data(){
          return {

              /*定义全局booklist*/
                foodlist:[{
                "name":"野蘑菇炖鸡",
                "img":"./static/images/mogu_ji.png",
                "price":58.00
              },{
                "name":"大盘鸡",
                "img":"./static/images/dapan_ji.png",
                "price":62.00
              },
              {
                "name":"爆椒鸡",
                "img":"./static/images/baojiao_ji.png",
                "price":48.00
              },{
                "name":"辣子鸡丁",
                "img":"./static/images/lazi_ji.png",
                "price":39.00
              },
              {
                "name":"麻辣鱼头",
                "img":"./static/images/mala_yu.png",
                "price":52.00
              },{
                "name":"酸菜鱼",
                "img":"./static/images/lazi_ji.png",
                "price":53.00
              },
              {
                "name":"红烧带鱼",
                "img":"./static/images/mala_yu.png",
                "price":42.00
              },{
                "name":"水煮肉片",
                "img":"./static/images/dapan_ji.png",
                "price":35.00
              },
              {
                "name":"毛血旺",
                "img":"./static/images/baojiao_ji.png",
                "price":30.00
              },{
                "name":"鱼香肉丝",
                "img":"./static/images/lazi_ji.png",
                "price":18.00
              },
              {
                "name":"烧大肠",
                "img":"./static/images/mala_yu.png",
                "price":28.00
              },{
                "name":"农家小炒肉",
                "img":"./static/images/lazi_ji.png",
                "price":25.00
              },
              {
                "name":"青椒肉丝",
                "img":"./static/images/mala_yu.png",
                "price":20.00
              },{
                "name":"京酱肉丝",
                "img":"./static/images/mala_yu.png",
                "price":19.00
              },{
                "name":"红烧肉（带饼）",
                "img":"./static/images/lazi_ji.png",
                "price":30.00
              },
              {
                "name":"回锅肉",
                "img":"./static/images/mala_yu.png",
                "price":16.00
              },{
                "name":"木须肉",
                "img":"./static/images/mala_yu.png",
                "price":18.00
              },{
                "name":"酸豆角炒肉末",
                "img":"./static/images/lazi_ji.png",
                "price":22.00
              },
              {
                "name":"鲜辣烤鱼",
                "img":"./static/images/mala_yu.png",
                "price":79.00
              },{
                "name":"干锅菜花",
                "img":"./static/images/mala_yu.png",
                "price":16.00
              },{
                "name":"干锅千页豆腐",
                "img":"./static/images/lazi_ji.png",
                "price":15.00
              },
              {
                "name":"西红柿烧牛楠",
                "img":"./static/images/mala_yu.png",
                "price":29.00
              },{
                "name":"绿豆牙炒馓子",
                "img":"./static/images/mala_yu.png",
                "price":13.00
              },{
                "name":"西红柿炒鸡蛋",
                "img":"./static/images/lazi_ji.png",
                "price":12.00
              },
              {
                "name":"酸辣土豆丝",
                "img":"./static/images/mala_yu.png",
                "price":14.00
              },{
                "name":"香菇青菜",
                "img":"./static/images/mala_yu.png",
                "price":17.00
              },{
                "name":"麻辣豆腐",
                "img":"./static/images/lazi_ji.png",
                "price":10.00
              },
              {
                "name":"鱼香茄子",
                "img":"./static/images/mala_yu.png",
                "price":15.00
              },{
                "name":"爆炒花哈",
                "img":"./static/images/mala_yu.png",
                "price":23.00
              },{
                "name":"豆芽粉条",
                "img":"./static/images/lazi_ji.png",
                "price":11.00
              },
              {
                "name":"红油耳丝",
                "img":"./static/images/mala_yu.png",
                "price":16.00
              },{
                "name":"变蛋黄豆",
                "img":"./static/images/mala_yu.png",
                "price":9.00
              },{
                "name":"麻辣花生米",
                "img":"./static/images/lazi_ji.png",
                "price":9.00
              },
              {
                "name":"水蒸蛋",
                "img":"./static/images/mala_yu.png",
                "price":10.00
              },{
                "name":"烧茄子",
                "img":"./static/images/mala_yu.png",
                "price":14.00
              },{
                "name":"炒饼丝",
                "img":"./static/images/lazi_ji.png",
                "price":8.00
              }],
               tableData: [],
                currentPage: 1,
                pageSize: 2,
                totalPage: 0
          }
   },
  created() {
      this.totalPage = this.foodlist.length / this.pageSize
      this.loadData()
  },
  mounted() {
      this.tableListener()
  },
  methods: {
            loadData() {

                //这里模拟请求数据，最后一页数据不够pageSize时有BUG，暂不处理
                let data = this.foodlist.splice((this.currentPage - 1) * this.pageSize, this.pageSize)
                this.tableData = this.tableData.concat(data);
                console.log("表格数据量：",this.tableData.length)
            },
            tableListener() {
                console.log("监听表格dom对象的滚动事件")
                let that = this;
                let dom = that.$refs.myTable.bodyWrapper
                dom.addEventListener("scroll", function () {
                    const scrollDistance = dom.scrollHeight - dom.scrollTop - dom.clientHeight;
                    console.log("scroll", scrollDistance)
                    if (scrollDistance <= 0) {//等于0证明已经到底，可以请求接口
                        if (that.currentPage < that.totalPage) {//当前页数小于总页数就请求
                            that.currentPage++;//当前页数自增
                            //请求接口的代码
                            that.loadData()
                        }
                    }
                })
            }
   }
}
</script>


<style scoped>
  .el-header{
    background-color:darkgreen;
    color:white;
    line-height:60px;
    font-size:20px;
  }
  .el-menu-item:hover{
      background:yellow!important;
      color:purple!important;

  }
  .el-menu-item.is-active{
      background:purple!important;
      color:white!important;

  }
  .el-icon-cart{
     width:60px;
     height:60px;
     background: url("../assets/image/cart.png") center no-repeat;
     background-size:100% 100%;
     margin-top:-10px;
  }
  .el-icon-cart:before{
    visibility: hidden;
  }
  .bg-green-dark{
    background-color:black;
    height:60px;
    line-height:60px;
    color:white;
  }
  .bg-red-dark{
    background-color:darkred;
    color:white;
    height:60px;
    line-height:60px;
  }
</style>
