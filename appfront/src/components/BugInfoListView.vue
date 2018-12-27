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
        <td class="col-3"><textarea class="form-control">{{item.desc}}</textarea></td>
        <td class="col-1">
          <div class="btn-group">
            <button type="button" class="btn dropdown-toggle btn-sm btn-secondary" data-toggle="dropdown">
              {{item.level}}
            </button>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="#">严重</a>
              <a class="dropdown-item" href="#">中等</a>
              <a class="dropdown-item" href="#">甚微</a>
            </div>
          </div>
        </td>
        <td class="col-3"><textarea class="form-control">{{item.way}}</textarea></td>
        <td class="col-1">
          <div class="btn-group">
            <button type="button" class="btn dropdown-toggle btn-sm btn-secondary" data-toggle="dropdown">
              {{item.result}}
            </button>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="#">通过</a>
              <a class="dropdown-item" href="#">未测</a>
            </div>
          </div>
        </td>
        <td class="col-2">
          <div class="btn-group">
            <button type="button" class="btn dropdown-toggle  btn-secondary btn-sm" data-toggle="dropdown">
              {{item.man}}
            </button>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="#">刘书成</a>
              <a class="dropdown-item" href="#">海境</a>
              <a class="dropdown-item" href="#">李仁伟</a>
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
    <button type="submit" class="btn btn-secondary btn-lg" @click="look">预览</button>
  </div>
</template>

<script>
  export default {
    name: "BugInfoListView",
    data() {
      return {
        buglist: [{'desc': '这是一个bug', 'level': '中等', 'way': '没有修复方案', 'result': '通过', 'man': '海境'},
          {'desc': '这是一个bug', 'level': '甚微', 'way': '没有修复方案', 'result': '通过', 'man': '海境'}]
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
      }
    }

  }
</script>

<style scoped>

</style>
