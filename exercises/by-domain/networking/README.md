# Services & Networking (20%)

Exercises covering services, ingress, network policies, and networking concepts.

## Tasks

1. **task-ingress** - Ingress resource creation
   - Create Ingress resource
   - Configure paths and services
   - Set up ingress rules

2. **task-networkpolicy** - NetworkPolicy configuration
   - Create NetworkPolicy
   - Configure ingress/egress rules
   - Set pod selectors and namespace selectors

3. **task-service-nodeport** - Service creation (NodePort)
   - Create Service
   - Configure NodePort
   - Set up service selectors

4. **task-ingress-simple** - Simple Ingress resource
   - Create basic Ingress
   - Single host and path
   - Imperative command

5. **task-ingress-multi-path** - Ingress with multiple paths and hosts
   - Multiple paths on same host
   - Multiple hosts
   - Path-based routing

6. **task-ingress-path-rewrite** - Ingress path rewriting
   - Rewrite URL paths
   - Use annotations
   - Path transformation

7. **task-networkpolicy-frontend-backend** - NetworkPolicy for frontend-backend
   - Allow ingress from frontend namespace
   - Port-specific rules
   - Cross-namespace communication

8. **task-networkpolicy-database-admin** - Restrict database access
   - Allow only admin pod access
   - Default deny policy
   - Pod selector rules

9. **task-networkpolicy-egress-cidr** - Egress to CIDR range
   - Allow egress to IP ranges
   - CIDR block configuration
   - External access

10. **task-networkpolicy-app-db** - App to database on specific port
    - Allow app namespace to db namespace
    - Port 3306 (MySQL) only
    - Namespace and pod selectors

11. **task-networkpolicy-allow-all** - Allow all traffic in namespace
    - Permissive NetworkPolicy
    - Allow all ingress and egress
    - Namespace-wide policy

12. **task-dns-lookup** - DNS lookup for services and pods
    - Service DNS records
    - Pod DNS records
    - Use nslookup utility

## Key Concepts

- **Services**: ClusterIP, NodePort, LoadBalancer
- **Ingress**: HTTP/HTTPS routing to services
- **NetworkPolicy**: Network traffic rules
- **CoreDNS**: Cluster DNS service
- **Gateway API**: Newer ingress API

## Practice Tips

- Understand different service types and when to use them
- Master NetworkPolicy creation (commonly tested)
- Practice Ingress configuration
- Know how to debug networking issues

---

**Exam Weight**: 20% - Important for exam success
