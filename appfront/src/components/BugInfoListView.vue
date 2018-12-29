<template>
  <div>
    <h5>Step 2:问题列表({{buglist.length}}个)</h5>
    <!--  table -->
    <table class="table table-striped row mx-0">
      <thead class="w-100">
      <tr class="row mx-0">
        <th class="col-1">序号</th>
        <th class="col-3">问题描述</th>
        <th class="col-1">等级</th>
        <th class="col-3">修复方案</th>
        <th class="col-1">自测结果</th>
        <th class="col-2">签名</th>
        <th class="col-1">操作</th>
      </tr>
      </thead>
      <tbody class="w-100">
      <tr v-for="(item,index) in buglist" class="row mx-0">
        <td class="col-1">{{index}}</td>
        <td class="col-3"><textarea class="form-control" v-model="item.desc"></textarea></td>
        <td class="col-1">
          <div class="btn-group">
            <button type="button" class="btn dropdown-toggle btn-sm btn-secondary" data-toggle="dropdown"
                    v-text="item.level">
            </button>
            <div class="dropdown-menu">

              <a class="dropdown-item" href="javascript:void(0)" v-for="item in levellist" v-text="item"
                 @click="selectLevel(item,index)"></a>
            </div>
          </div>
        </td>
        <td class="col-3"><textarea class="form-control" v-model="item.way"></textarea></td>
        <td class="col-1">
          <div class="btn-group">
            <button type="button" class="btn dropdown-toggle btn-sm btn-secondary" data-toggle="dropdown"
                    v-text="item.result">
            </button>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="javascript:void(0)" v-for="item in resultlist" v-text="item"
                 @click="selectResult(item,index)"></a>
            </div>
          </div>
        </td>
        <td class="col-2">
          <div class="btn-group">
            <button type="button" class="btn dropdown-toggle  btn-secondary btn-sm" data-toggle="dropdown"
                    v-text="item.man">
            </button>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="javascript:void(0)" v-for="item in manlist" v-text="item"
                 @click="selectMan(item,index)"></a>
            </div>
          </div>
        </td>
        <td class="col-1">
          <button class="btn btn-danger btn-sm" @click="delItem(index)">删除</button>
        </td>
      </tr>
      </tbody>
    </table>
    <!-- End table -->
    <button type="submit" class="btn btn-info btn-sm" @click="addItem">添加一条</button>
    <hr>
    <button type="submit" class="btn btn-primary btn-lg"><span class="glyphicon glyphicon-user"></span>保存</button>
    <button type="submit" class="btn btn-secondary btn-lg" @click="look" data-toggle="modal" data-target="#myModal">预览
    </button>
    <!-- 模态框 -->
    <div class="modal fade" id="myModal">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">

          <!-- 模态框头部 -->
          <div class="modal-header">
            <h4 class="modal-title">版本说明书</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
          </div>
          <!-- 模态框主体 -->
          <div class="modal-body">
            <bug-info-view></bug-info-view>
          </div>
          <!-- 模态框底部 -->
          <div class="modal-footer">
            <button type="button" class="btn btn-success" data-dismiss="modal">发送邮件</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import BugInfoView from '../components/BugInfoView'

  export default {
    name: "BugInfoListView",
    components: {BugInfoView},
    data() {
      return {
        buglist: [{'desc': '这是一个bug', 'level': '中等', 'way': '没有修复方案', 'result': '通过', 'man': '海境'},
          {'desc': '这是一个bug', 'level': '甚微', 'way': '没有修复方案', 'result': '通过', 'man': '海境'}],
        manlist: ['海境', '李仁伟', '饶正勇'],
        resultlist: ['通过', '未测'],
        levellist: ['严重', '中等', '甚微']
      }
    },
    methods: {
      addItem() {
        this.buglist.push({'desc': '', 'level': '中等', 'way': '', 'result': '通过', 'man': '海境'})
      },
      delItem(index) {
        this.buglist.splice(index, 1)
      },
      look() {
        console.log(this.buglist)
      },
      selectMan(man, index) {
        this.buglist[index].man = man
      },
      selectResult(result, index) {
        this.buglist[index].result = result
      },
      selectLevel(level, index) {
        this.buglist[index].level = level
      }
    }

  }
</script>

<style scoped>

</style>
