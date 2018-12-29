<template>
  <div>
    <table class="table table-bordered row mx-0 table-sm">
      <tbody class="w-100">
      <tr class="row mx-0">
        <td class="col-2 table-active">提交版本</td>
        <td class="col-4">V5.0.0(20181129-1)</td>
        <td class="col-2 table-active">提交日期</td>
        <td class="col-4">11/29/18</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-2 table-active">打包名称</td>
        <td class="col-4">国元iOS_测试V5.0.0(20181129-1).ipa</td>
        <td class="col-2 table-active">认证服务器地址</td>
        <td class="col-4">42.51.11.33:8080</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-2 table-active">环境选择</td>
        <td class="col-4">测试环境</td>
        <td class="col-2 table-active">券商代码</td>
        <td class="col-4">101</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-2 table-active">bundleId(包名)</td>
        <td class="col-4">com.qianlong.guoyuan</td>
        <td class="col-2 table-active">项目描述</td>
        <td class="col-4">国元iOS</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-2 table-active">版本</td>
        <td class="col-4">V5.0.1</td>
        <td class="col-2 table-active">SVNRevison</td>
        <td class="col-4">1223</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-2 table-active">提交包文件地址</td>
        <td class="col-10">http://42.51.11.33:8080/svn/qqbapk/东兴期权宝/test/东兴期权宝Android_测试V5.1.0.34(20181227-1).apk</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-2 table-active">修改/升级影响</td>
        <td class="col-10">没有影响</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-1 table-active">序号</td>
        <td class="col-4 table-active">问题描述</td>
        <td class="col-1 table-active">等级</td>
        <td class="col-3 table-active">修复方案</td>
        <td class="col-2 table-active">自测结果</td>
        <td class="col-1 table-active">签名</td>
      </tr>
      <tr class="row mx-0">
        <td class="col-1">1</td>
        <td class="col-4"><p style="font-size:15px">交易-下单进入委托下单页面，代码输入框里输入波指名称会搜索到波指列表</p></td>
        <td class="col-1">中等</td>
        <td class="col-3"><p style="font-size:15px">发生原因:客户端未做筛选 <br>修改方案:客户端做筛选，删除波指</p></td>
        <td class="col-2">通过</td>
        <td class="col-1"><p style="font-size:15px">海境</p></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: "BugInfoView"
  }
</script>

<style scoped>

</style>
