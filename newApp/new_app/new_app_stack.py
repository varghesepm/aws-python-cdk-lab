from aws_cdk import (
    core as cdk, 
    aws_s3 as _s3,
    aws_ec2 as _ec2,
    aws_ecs_patterns as _ecsp,
    aws_elasticloadbalancingv2 as _lb
)

#from aws_cdk import core


class NewAppStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        appVpc = _ec2.Vpc(self, "examVPC", cidr="10.0.0.0/16")

        bucket = _s3.Bucket(self, "lb-log-may20", bucket_name="test-lb-log-may20")

        #core.CfnOutput(self, "buckName", value=bucket.bucket_name)

        mylb = _lb.ApplicationLoadBalancer(self, "LB",
            vpc=appVpc,
            internet_facing=True
        )
        listener = mylb.add_listener("Listener",
            port=80,
            open=True
        )

        accessLog = mylb.log_access_logs(
            bucket=bucket
        )

        api = _ecsp.ApplicationLoadBalancedEc2Service(
                self,
                "my-service",
                service_name="service-a",
                cluster=self.cluster,
                cpu=512,
                memory_limit_mib=512,
                desired_count=4,
                domain_name="exampledomain.com",
                vpc=appVpc,
                loadBalancerName=mylb
       )
