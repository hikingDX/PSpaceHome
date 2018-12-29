<template>
  <div>
    <nav-header></nav-header>
    <div style="background-color: #e9ecef;">
      <div class="container" style="background-color: #e9ecef;">
        <ol class="breadcrumb">
          <li class="breadcrumb-item"><a href="#">首页</a></li>
          <li class="breadcrumb-item"><a href="#">版本说明书</a></li>
          <li class="breadcrumb-item"><a href="#">iOS</a></li>
          <li class="breadcrumb-item active"><a href="#">国元</a></li>
          <li class="breadcrumb-item active"><a href="#">测试</a></li>
          <li class="breadcrumb-item active">国元20181212_1测试</li>
        </ol>
      </div>
    </div>
    <div class="container">
      <h5>Step 1:基本信息</h5>
      <table class="table table-striped ">
        <thead>
        <tr>
          <th>名称</th>
          <th>内容</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td>提交版本</td>
          <td v-model="subVersion"></td>
        </tr>
        <tr>
          <td>提交日期</td>
          <td v-model="subDate"></td>
        </tr>
        <tr>
          <td>打包名称</td>
          <td v-model="subName"></td>
        </tr>
        <tr>
          <td>环境选择</td>
          <td v-model="env"></td>
        </tr>
        <tr>
          <td>券商代码</td>
          <td>101</td>
        </tr>
        <tr>
          <td>bundleId(包名)</td>
          <td>com.qianlong.guoyuan</td>
        </tr>
        <tr>
          <td>项目描述</td>
          <td>国元iOS</td>
        </tr>
        <tr>
          <td>提交包文件地址</td>
          <td>http://42.51.11.33:8080/svn/qqbapk/东兴期权宝/test/东兴期权宝Android_测试V5.1.0.34(20181227-1).apk</td>
        </tr>
        <tr>
          <td>版本</td>
          <td><input type="email" class="form-control" id="email"></td>
        </tr>
        <tr>
          <td>SVNRevison</td>
          <td><input type="email" class="form-control" id="email"></td>
        </tr>
        <tr>
          <td>认证服务器地址</td>
          <td><input type="email" class="form-control" id="email"></td>
        </tr>
        <tr>
          <td>修改/升级影响</td>
          <td><input type="email" class="form-control" id="email"></td>
        </tr>
        </tbody>
      </table>
      <bug-info-list-view></bug-info-list-view>
      <hr>
    </div>
  </div>
</template>

<script>
  import NavHeader from './../components/NavHeader'
  import BugInfoListView from '../components/BugInfoListView'

  export default {
    name: "Index",
    data() {
      return {
        subVersion:'V5.0.0(20181129-1)',
        subDate:'11/29/18',
        subName:'国元iOS_测试V5.0.0(20181129-1).ipa',
        env:'测试环境',
        trader
      }
    },
    components: {
      BugInfoListView,
      NavHeader
    }
  }
</script>

<style scoped>

</style>
