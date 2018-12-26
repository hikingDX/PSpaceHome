<template>
  <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container">
      <a class="navbar-brand" href="/">QLMobile</a>
      <!-- Links -->
      <ul class="navbar-nav justify-content-center">
        <li class="nav-item">
          <a class="nav-link" href="#">Link 1</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link 2</a>
        </li>

        <!-- Dropdown -->
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
            工具
          </a>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="#">版本说明书生成器</a>
            <a class="dropdown-item" href="#">Link 2</a>
            <a class="dropdown-item" href="#">Link 3</a>
          </div>
        </li>
      </ul>
      <form class="form-inline navbar-left justify-content-center">
        <input class="form-control" type="text" placeholder="Search">
      </form>
      <ul class="navbar-nav justify-content-end" id="headerNav">
        <li class="nav-item" id="navMainPage"><a class="nav-link" href="/"> 设置 </a></li>
        <li class="nav-item">
          <a href="#" class="nav-link">消息
            <span class="badge" id="mybadge" style="background-color: #ec7063">10</span>
          </a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown">
            个人
          </a>
          <ul class="dropdown-menu">
            <a class="dropdown-item" href="#">Link 1</a>
            <a class="dropdown-item" href="#">Link 2</a>
            <a class="dropdown-item" href="#">Link 3</a>
          </ul>
        </li>
      </ul>
    </div>

  </nav>
</template>

<script>
  export default {
    name: "NavHeader"
  }
</script>

<style scoped>

</style>
