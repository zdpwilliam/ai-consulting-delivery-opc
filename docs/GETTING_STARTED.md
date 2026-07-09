# 🚀 快速开始指南

## 前置要求

- Python 3.9 或更高版本
- pip 包管理器
- Git 版本控制
- 有效的API密钥（Claude/OpenAI）

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/zdpwilliam/ai-consulting-delivery-opc.git
cd ai-consulting-delivery-opc
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 API 密钥
```

## 快速演示

### 示例1: 销售Agent

```python
from agents.sales_agent import SalesAgent

# 初始化销售agent
sales_agent = SalesAgent()

# 运行销售流程
result = sales_agent.process_lead({
    "client_name": "Acme Corp",
    "email": "contact@acme.com",
    "inquiry": "We need AI consulting for our e-commerce platform"
})

print(result)
```

### 示例2: 法律合规检查

```python
from skills.legal.contract_review_skill import ContractReviewSkill

# 初始化合规检查
legal_skill = ContractReviewSkill()

# 分析合同
analysis = legal_skill.review_contract(
    contract_text=your_contract_text,
    jurisdiction="US"
)

print(analysis)
```

## 项目结构

```
ai-consulting-delivery-opc/
├── agents/               # 代理定义
├── skills/              # 行业特定技能
├── workflows/           # 工作流管理
├── integrations/        # 外部集成
├── config/              # 配置文件
├── tests/               # 测试
└── docs/                # 文档
```

## 常见问题

**Q: 如何添加新的行业Skill？**

A: 在 `skills/` 目录下创建新文件夹，参考现有的行业实现。

**Q: 如何集成我的CRM？**

A: 参考 `integrations/crm_connector.py` 中的实现。

**Q: 如何部署到生产环境？**

A: 参考 `docs/DEPLOYMENT_GUIDE.md`。

## 学习资源

- [完整总结](COMPREHENSIVE_SUMMARY.md)
- [系统架构](ARCHITECTURE.md)
- [部署指南](DEPLOYMENT_GUIDE.md)
