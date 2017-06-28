var plan = require('./index')

plan.target('test',
[
  {
    host: 'nohost',
    failsafe: true,
    user: 'root'
  },
  {
    host: 'kube2.pstadler.io',
    port: 22,
    user: 'pstadler',
    agent: process.env.SSH_AUTH_SOCK,
    password: 'foo',
    failsafe: true
  },
  {
    host: 'kube3.pstadler.io',
    port: 22,
    user: 'root',
    failsafe: true
  },
  {
    host: 'foobarfofofo',
    failsafe: true,
    agent: 'process.env.SSH_AUTH_SOCK',
    user: 'root'
  },
  {
    host: 'localhost',
    failsafe: true,
    username: 'pstadler',
    agent: 'process.env.SSH_AUTH_SOCK'
  }
])

plan.remote(function (remote) {
  remote.exec('ls -al')
})
