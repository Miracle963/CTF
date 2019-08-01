"整理CTF题目" 

```shell
echo "# CTF" >> README.md
git init
git add README.md # 将本地文件在init好后添加到push 队列
git commit -m "first commit" # 添加上传注释
git remote add origin https://github.com/thonsun/CTF.git # 目标
git push -u origin master # 以什么身份进行上传  这次是真正的开始push(把队列中的文件一个个上传)
```

